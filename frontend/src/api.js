export async function getPolygons(){
  const base = import.meta.env.VITE_API_BASE || '/api'
  const res = await fetch(`${base}/polygons/`)
  return res.json()
}
