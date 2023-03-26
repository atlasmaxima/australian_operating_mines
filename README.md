# Australian Operating Mines

## Datasets 
https://catalogue.data.wa.gov.au/dataset/operating-mines

## Improvement 
- Large dataset, Google Maps has trouble rendering it, performance would need to be resolved.
- Utilise tectonic unit to see a 3D rendered visualisation
- Improve on markers with modal with commodities  
- TDD

## Purpose
Reference: https://portal.ga.gov.au/persona/minesatlas
- Provide a better and more elegant visualisation to make better business decisions for resources and energy industries.

---
## Local Setup
### `env`
```bash
export GOOGLE_MAP_API={google_api_key}
```

Set up a python virtual environment 
[conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

All the dependencies are in `environment.yml`

### `flask run`
```bash
cd /Flask
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```
---
### `npm install`
Install dependencies 

### `npm start`
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.


