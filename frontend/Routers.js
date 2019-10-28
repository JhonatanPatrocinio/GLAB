import { Router, Scene, Actions, ActionConst, Drawer } from 'react-native-router-flux'
import React, { Component } from 'react';

import perfilProf from './screens/perfilProf'
import editarProf from './screens/editarProf'
import cadastro from './screens/cadastro'

export default class Routers extends Component {

  render() {
    return (
      <Router>
        <Drawer>

          <Scene 
            key="root"
            title='Menu'
            headerLayoutPreset='center'>





            <Scene
              key={'Cadastro'}
              component={cadastro} />
            <Scene
              key={'PerfilProf'}
              component={perfilProf} />
            <Scene
              key={'EditarProf'}
              component={editarProf} />





          </Scene>

        </Drawer>
      </Router>


    );

  }
}




import React, { Component } from 'react';


import Routers from './Routers'






export default class App extends Component {

  render() {
    return (
      <Routers />
    );

  }
}
