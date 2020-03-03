import {
  CHANGE_BREADCRUMB_ACTION,
  CHANGE_LOADING_ACTION,
  CHANGE_MAIN_TITLE_ACTION,
  CHANGE_MESSAGE_ACTION
} from './actions'

export const layoutReducer = (state, action) => {
  switch (action.type) {
    case CHANGE_MAIN_TITLE_ACTION:
      return {...state, title: action.title}

    case CHANGE_LOADING_ACTION:
      return {...state, loading: action.isLoading}

    case CHANGE_BREADCRUMB_ACTION:
      return {...state, breadcrumbs: action.breadcrumbs}

    case CHANGE_MESSAGE_ACTION:
      return {...state, message: action.message}

    default:
      return state
  }
}
