import './style.css'
import maplibregl from 'maplibre-gl'
import { getPolygons } from './api'

const map = new maplibregl.Map({
  container: 'app',
  style: {
    version: 8,
    sources: {
      osm: { type: 'raster', tiles: [import.meta.env.VITE_TILES_URL], tileSize: 256 }
    },
    layers: [{ id: 'osm', type: 'raster', source: 'osm' }]
  },
  center: [-68.879, -33.054],
  zoom: 10
})

getPolygons().then(data => {
  map.addSource('exposure', { type: 'geojson', data })
  map.addLayer({ id: 'exposure', type: 'fill', source: 'exposure', paint: { 'fill-color': '#f00', 'fill-opacity': 0.5 } })
})
