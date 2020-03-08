import React, { createContext, useContext, useReducer } from 'react'

export const AppContext = createContext()
export const AppStateStore = {
  dispatch: undefined
}

// Hook customizado para guardar uma referência da função "dispatch" (ou até
// mesmo do "state" caso necessário) para que seja usado em qualquer outro modulo
// ou nas actions assincronas, ou seja, actions que retornam uma função.
const useReducerAppHook = (reducer, initialState) => {
  const [state, dispatch] = useReducer(reducer, initialState)
  AppStateStore.dispatch = dispatch

  return [state, dispatch]
}

export const AppStateProvider = ({reducer, initialState, children}) => (
  <AppContext.Provider value={useReducerAppHook(reducer, initialState)}>
    {children}
  </AppContext.Provider>
)

export const useAppState = () => useContext(AppContext)