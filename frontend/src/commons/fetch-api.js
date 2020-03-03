let changeLoadingState = () => {
}
let changeMessage = () => {
}

class AppError extends Error {
  constructor(code, message) {
    super()
    this.message = message
    this.code = code
  }
}

function tratarRetornoChamadaApi(resp) {
  if (resp.type !== 'opaque' && !resp.ok && resp.status !== 400) {
    throw new AppError(
        resp.status,
        resp.statusText ? resp.statusText : 'Erro não identificado'
    )
  }

  return Promise.resolve(resp)
}

function getJson(response) {
  return response.json().catch(e => {
    console.error(e)
    return Promise.resolve({})
  })
}

function tratarDadosResposta(data, resp) {
  if (resp.status !== 200 && resp.status !== 201) {
    if (resp.status === 400) {
      changeMessage({type: 'ERROR', text: data.message})
      return Promise.resolve()
    }
    throw new AppError(data.code, data.message)
  }

  return Promise.resolve(data)
}

function tratarErro(error) {
  console.log(error)

  if (error instanceof AppError) {
    if (error.code === 401) {
      // TODO: Tratar nao logado
      changeMessage({type: 'ERROR', text: 'Usuário não autenticado'})
      return Promise.resolve()
    }
    if (error.code === 500) {
      changeMessage({
        type: 'ERROR',
        text: 'Problema no servidor do Minha Conta, tente novamente mais tarde.'
      })
      return Promise.resolve()
    }

    return Promise.reject(error)
  }

  throw new Error('Erro executando o comando fetch: ' + error.message)
}

export const setDependenciesFunctions = props => {
  changeLoadingState = props.changeLoadingState
  changeMessage = props.changeMessage
}

const fetchApi = async (url, options) => {
  if (options.method === 'POST') {
    options.headers = {
      'Content-Type': 'application/json'
    }
  }

  try {
    changeLoadingState(true)
    const resp = await fetch(url, options)
    changeLoadingState(false)

    const response = await tratarRetornoChamadaApi(resp)
    const data = await getJson(response)
    return await tratarDadosResposta(data, response)
  } catch (error) {
    changeLoadingState(false)
    return tratarErro(error)
  }
}

export default fetchApi
