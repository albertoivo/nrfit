import React from 'react'
import '../assets/styles.css'
import { useAppState } from './AppContext'
import LoadingOverlay from 'react-loading-overlay'

function App() {
  const [{layout}] = useAppState()

  return (
      <>
        <p>blah</p>
        <LoadingOverlay
            active={layout.loading}
            spinner
            text='Aguarde. Estamos processando suas informações'
            styles={
              {
                overlay: base => ({
                  ...base,
                  position: 'fixed'
                })
              }
            }
        />
      </>
  )
}

export default App
