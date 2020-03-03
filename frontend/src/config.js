import { setDependenciesFunctions } from './commons/fetch-api'
import { AppStateStore } from './components/AppContext'
import { loggedUserReducer } from './commons/logged-user/reducer'
import { layoutReducer } from './components/layout/reducer'
import { changeLoading, changeMessage } from './components/layout/actions'
import { INITIAL_STATE } from './commons/constants'

const Configurations = {
  configFetchApi: () => {
    setDependenciesFunctions({
      changeLoadingState: isLoading => {
        AppStateStore.dispatch(changeLoading(isLoading))
      },
      changeMessage: message => {
        AppStateStore.dispatch(changeMessage(message))
      }
    })
  },
  reducers: (state, action) => {
    if (typeof action === 'function') {
      // Chamada assíncrona das actions que são functions.
      setTimeout(() => {
        action(AppStateStore.dispatch, state)
      }, 0)
      return state
    }

    const newState = {
      logged_user: loggedUserReducer(state.logged_user, action),
      layout: layoutReducer(state.layout, action)
    }

    if (process.env.NODE_ENV !== 'production') {
      console.log('%c before: ' + JSON.stringify(state), 'color: gray')
      console.log('%c action: ' + JSON.stringify(action), 'color: blue')
      console.log('%c after: ' + JSON.stringify(newState), 'color: green')
    }

    return newState
  },
  initialState: INITIAL_STATE
}

export default Configurations
