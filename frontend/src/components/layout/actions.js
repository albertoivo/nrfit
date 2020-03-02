export const CHANGE_MAIN_TITLE_ACTION = 'LAYOUT/CHANGE_MAIN_TITLE'
export const CHANGE_LOADING_ACTION = 'LAYOUT/CHANGE_LOADING'
export const CHANGE_BREADCRUMB_ACTION = 'LAYOUT/CHANGE_BREADCRUMB'
export const CHANGE_MESSAGE_ACTION = 'LAYOUT/CHANGE_MESSAGE'

const changeMainTitle = title => ({
  type: CHANGE_MAIN_TITLE_ACTION,
  title
})

const changeBreadcrumb = breadcrumbs => ({
  type: CHANGE_BREADCRUMB_ACTION,
  breadcrumbs
})

export const changeInfoTela = ({title, breadcrumbs}) => (dispatch, state) => {
  dispatch(changeMainTitle(title))
  dispatch(changeBreadcrumb(breadcrumbs || []))

  // Limpa a mensagem mas apenas se não for definida como fixa pois
  // deseja-se preservar a mensagem inserida pela página anterior.
  if (state.layout.message && !state.layout.message.fixed) {
    dispatch(changeMessage({}))
  }
}

export const changeLoading = isLoading => ({
  type: CHANGE_LOADING_ACTION,
  isLoading
})

export const changeMessage = message => ({
  type: CHANGE_MESSAGE_ACTION,
  message
})

export const changeMessageDelay = message => dispatch => {
  dispatch(changeMessage(message))
  setTimeout(() => {
    dispatch(changeMessage({}))
  }, 7000)
}
