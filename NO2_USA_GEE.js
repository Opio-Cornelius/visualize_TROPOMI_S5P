var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2')
  .select('tropospheric_NO2_column_number_density')
  .filterDate('2018-07-01', '2019-12-31');

var clip = collection.mean().clip(geometry);

var band_viz = {
  min: 0,
  max: 0.0002,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};

Map.addLayer(collection.mean(), band_viz, 'S5P N02');
Map.setCenter(-97.9, 40.9, 3);

Export.image.toDrive({
  image: clip,
  description: 'NO2_tropomi_USA',
  folder: 'ATMSCIENCE_Projects',
  region: geometry,
  scale: 1000,
  crs: 'EPSG:4326',
  maxPixels: 1e10});
