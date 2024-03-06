var pureCoverage = false;
var format = 'image/png';
var supportsFiltering = true;
var map = null;
var bounds = null
var untiled = null;
var tiled = null;

// sets the chosen WMS version
function setWMSVersion(wmsVersion) {
  map.getLayers().forEach(function(lyr) {
    lyr.getSource().updateParams({'VERSION': wmsVersion});
  });
  if(wmsVersion == "1.3.0") {
      origin = bounds[1] + ',' + bounds[0];
  } else {
      origin = bounds[0] + ',' + bounds[1];
  }
  tiled.getSource().updateParams({'tilesOrigin': origin});
}

// Tiling mode, can be 'tiled' or 'untiled'
function setTileMode(tilingMode) {
  if (tilingMode == 'tiled') {
    untiled.set('visible', false);
    tiled.set('visible', true);
  } else {
    tiled.set('visible', false);
    untiled.set('visible', true);
  }
}

function setAntialiasMode(mode) {
  map.getLayers().forEach(function(lyr) {
    lyr.getSource().updateParams({'FORMAT_OPTIONS': 'antialias:' + mode});
  });
}

// changes the current tile format
function setImageFormat(mime) {
  map.getLayers().forEach(function(lyr) {
    lyr.getSource().updateParams({'FORMAT': mime});
  });
}

function setStyle(style){
  map.getLayers().forEach(function(lyr) {
    lyr.getSource().updateParams({'STYLES': style});
  });
}

function setWidth(size){
  var mapDiv = document.getElementById('map');
  var wrapper = document.getElementById('wrapper');

  if (size == "auto") {
    // reset back to the default value
    mapDiv.style.width = null;
    wrapper.style.width = null;
  }
  else {
    mapDiv.style.width = size + "px";
    wrapper.style.width = size + "px";
  }
  // notify OL that we changed the size of the map div
  map.updateSize();
}

function setHeight(size){
  var mapDiv = document.getElementById('map');
  if (size == "auto") {
    // reset back to the default value
    mapDiv.style.height = null;
  }
  else {
    mapDiv.style.height = size + "px";
  }
  // notify OL that we changed the size of the map div
  map.updateSize();
}

function updateFilter(){
  if (!supportsFiltering) {
    return;
  }
  var filterType = document.getElementById('filterType').value;
  var filter = document.getElementById('filter').value;
  // by default, reset all filters
  var filterParams = {
    'FILTER': null,
    'CQL_FILTER': null,
    'FEATUREID': null
  };
  if (filter.replace(/^\s\s*/, '').replace(/\s\s*$/, '') != "") {
    if (filterType == "cql") {
      filterParams["CQL_FILTER"] = filter;
    }
    if (filterType == "ogc") {
      filterParams["FILTER"] = filter;
    }
    if (filterType == "fid")
      filterParams["FEATUREID"] = filter;
    }
    // merge the new filter definitions
    map.getLayers().forEach(function(lyr) {
      lyr.getSource().updateParams(filterParams);
    });
  }

  function resetFilter() {
    if (!supportsFiltering) {
      return;
    }
    document.getElementById('filter').value = "";
    updateFilter();
  }

  // shows/hide the control panel
  function toggleControlPanel(){
    var toolbar = document.getElementById("toolbar");
    if (toolbar.style.display == "none") {
      toolbar.style.display = "block";
    }
    else {
      toolbar.style.display = "none";
    }
    map.updateSize()
  }

  function initMap(bb1, bb2, bb3, bb4, resourceid, title) {
    pureCoverage = false;
    format = 'image/png';
    
    bounds = [bb4, bb1, bb2, bb3];
    if (pureCoverage) {
      document.getElementById('antialiasSelector').disabled = true;
      document.getElementById('jpeg').selected = true;
      format = "image/jpeg";
    }
  
    supportsFiltering = true;
    if (!supportsFiltering) {
      document.getElementById('filterType').disabled = true;
      document.getElementById('filter').disabled = true;
      document.getElementById('updateFilterButton').disabled = true;
      document.getElementById('resetFilterButton').disabled = true;
    }
  
    var mousePositionControl = new ol.control.MousePosition({
      className: 'custom-mouse-position',
      target: document.getElementById('location'),
      coordinateFormat: ol.coordinate.createStringXY(5),
      undefinedHTML: '&nbsp;'
    });
  
    untiled = new ol.layer.Image({
      source: new ol.source.ImageWMS({
        ratio: 1,
        url: `https://geoserver.hydroshare.org/geoserver/${resourceid}/wms`,
        params: {
          'FORMAT': format,
          'VERSION': '1.1.1',
          "LAYERS": `${resourceid}:${title}`,
          "exceptions": 'application/vnd.ogc.se_inimage',
        }
      })
    });
  
    tiled = new ol.layer.Tile({
      visible: false,
      source: new ol.source.TileWMS({
        url: `https://geoserver.hydroshare.org/geoserver/${resourceid}/wms`,
        params: {
          'FORMAT': format,
          'VERSION': '1.1.1',
          tiled: true,
          "LAYERS": `${resourceid}:${title}`,
          "exceptions": 'application/vnd.ogc.se_inimage',
          tilesOrigin: bb4 + "," + bb1
        }
      })
    });
  
    var projection = new ol.proj.Projection({
      code: 'EPSG:4269',
      units: 'degrees',
      axisOrientation: 'neu',
      global: true
    });
  
    map = new ol.Map({
      controls: ol.control.defaults({
        attribution: false
      }).extend([mousePositionControl]),
      target: 'map',
      layers: [untiled, tiled],
      view: new ol.View({
        projection: projection
      })
    });
  
    map.getView().fit(bounds, map.getSize());
    map.getView().on('change:resolution', function(evt) {
        var resolution = evt.target.get('resolution');
        var units = map.getView().getProjection().getUnits();
        var dpi = 25.4 / 0.28;
        var mpu = ol.proj.METERS_PER_UNIT[units];
        var scale = resolution * mpu * 39.37 * dpi;
        if (scale >= 9500 && scale <= 950000) {
          scale = Math.round(scale / 1000) + "K";
        } else if (scale >= 950000) {
          scale = Math.round(scale / 1000000) + "M";
        } else {
          scale = Math.round(scale);
        }
        document.getElementById('scale').innerHTML = "Scale = 1 : " + scale;
      });
      map.getView().fit(bounds, map.getSize());
      map.on('singleclick', async function(evt) {
        document.getElementById('nodelist').innerHTML = "Loading... please wait...";
        var view = map.getView();
        var viewResolution = view.getResolution();
        var source = untiled.get('visible') ? untiled.getSource() : tiled.getSource();
        var url = source.getGetFeatureInfoUrl(
          evt.coordinate, viewResolution, view.getProjection(),
          {'INFO_FORMAT': 'text/html', 'FEATURE_COUNT': 50});
          // console.log(url)
        if (url) {
            const geoserver_table_url = document.getElementById('loading-geserver-table-url').getAttribute("data-url");
            const response = await fetch(`${geoserver_table_url}?url=${btoa(url)}`);
            const response_json = await response.json();
            // console.log(response_json)
            document.getElementById('nodelist').innerHTML =response_json['content'] ;
        }
      });
  
  }
  
  function destroyMap() {
    map = null;
    bounds = null;
    tiled = null;
    untiled = null;
    document.getElementById('wrapper-map').style.display = 'none'
    const mapElement = document.getElementById('map')
    if (mapElement) {
      mapElement.innerHTML = ''; // This removes all child elements
      document.getElementById('nodelist').innerHTML = ''
    }
  
  }
let resourceslist = []


let button = document.getElementById('fetchfile')
const fileSelector = document.querySelector('#title_input')
button.addEventListener('click', async function () {
    const username = document.getElementById('username')
    const password = document.getElementById('password')
    const viewr = document.getElementById('viewr')
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')

    const formData = new FormData();
    formData.append('username', username && username.value);
    formData.append('password', password && password.value);
    formData.append('viewr', viewr.value);
    formData.append('csrfmiddlewaretoken', csrfToken.value);

    document.body.classList.add('waiting');
    let responseData;
    try{
        const response = await fetch('.', {
            method: 'post',
            body: formData
        });

        responseData = await response.json()
    } catch{

    }finally{
        document.body.classList.remove('waiting');
    }resourceslist = responseData

    var child = fileSelector.lastElementChild;
    while (child) {
        fileSelector.removeChild(child);
        child = fileSelector.lastElementChild;
    }
    const filteredresource = responseData.filter(resource=>{
        
        if(!resource.coverages || resource.coverages.length==0){
            return false
        }
        const box = resource.coverages.find(coveragesItem=>coveragesItem.type=="box")
        if (box){return true}
        return false
    })
    // Default option
    const option = document.createElement('option');
    option.textContent = filteredresource.length==0?"THE SUBJECT YOU SEARCHED FOR DOES NOT HAVE RESOURCES WITH A SHAPEFILE":"Select a Resource";
    fileSelector.append(option)

    // File name options
    filteredresource.forEach(result => {
        const option = document.createElement('option');
        option.value = result.resource_id;
        option.textContent = result.resource_title;
        fileSelector.append(option)
    })
})
fileSelector.addEventListener('change', function(event){
    const selected = document.querySelector('#selected_resource')
    selected.textContent = event.target.value
})

const viewbutton = document.querySelector('[name=add-button]')
viewbutton.addEventListener('click', async function(event){
    event.preventDefault()
    const selectedid = fileSelector.value
    const resource = resourceslist.find(resource=>resource.resource_id==selectedid)



    if(resource){

        // please convert to vanilla js the following
        const random_url = document.getElementById('random-url').getAttribute("data-url");
        // console.log(random_url)
        const response = await fetch(`${random_url}?id=${selectedid}`, {
            method: 'get'
        });
        // console.log(response)
        
        let responseData = await response.json()
        destroyMap()
        document.getElementById('wrapper-map').style.display = 'block'
        initMap(responseData.bb1, responseData.bb2, responseData.bb3, responseData.bb4, responseData.resourceid, responseData.title)
        // console.log(responseData)

    }
})


