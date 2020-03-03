import { CHANGE_LOGGED_USER_ACTION } from './actions'

export const loggedUserReducer = (state, action) => {
  switch (action.type) {
    case CHANGE_LOGGED_USER_ACTION:
      return {...state, ...action.user}

    default:
      return state
  }
}
