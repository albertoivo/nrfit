import React from 'react'
import ReactDOM from 'react-dom'
import App from './components/layout/App'
import * as serviceWorker from './serviceWorker'
import { BrowserRouter as Router } from 'react-router-dom'
import Configurations from './config'
import { AppStateProvider } from './components/AppContext'

const initialState = Configurations.initialState
const reducers = Configurations.reducers
Configurations.configFetchApi()

function Index() {
  return (
    <Router>
      <AppStateProvider initialState={initialState} reducer={reducers}>
        <App/>
      </AppStateProvider>
    </Router>
  )
}

ReactDOM.render(<Index/>, document.getElementById('root'))

serviceWorker.register()
