import React, { useEffect } from 'react'
import { useAppState } from '../AppContext'
import { fetchLoggedUser } from '../../commons/logged-user/actions'
import { changeInfoTela } from '../layout/actions'

const componentDidMount = (dispatch, state) => () => {
  dispatch(changeInfoTela({title: 'Bem-vindo(a)'}))
  if (!state.logged_user.id) {
    dispatch(fetchLoggedUser())
  }
}

function Init() {
  const [state, dispatch] = useAppState()
  useEffect(componentDidMount(dispatch, state), [])

  return (
      !state.logged_user.id && (
          <span>Usuário não encontrado!</span>
      )
  )
}

export default Init
