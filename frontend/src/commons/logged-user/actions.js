import fetchApi from '../fetch-api'
import { API_PATH } from '../constants'

export const CHANGE_LOGGED_USER_ACTION = 'USER/CHANGE_LOGGED_USER'

export const changeLoggedUserData = user => ({
  type: CHANGE_LOGGED_USER_ACTION,
  user
})

export const fetchLoggedUser = () => async dispatch => {
  const user = await fetchApi(API_PATH.fit.home, {
    method: 'GET'
  })

  dispatch(changeLoggedUserData(user))
}
