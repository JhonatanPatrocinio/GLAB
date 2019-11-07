import { createAppContainer, createSwitchNavigator } from 'react-navigation' 

import Login from './screens/telaLogin';
import Cadastro from './screens/cadastro';
import CadasAlu from './screens/cadastroAlun';
import CadasPro from './screens/cadastroProf';
import PerfilAlu from './screens/perfilAlun';
import PerfilPro from './screens/perfilProf';
import EditarAlu from './screens/editarAluno';
import EditarPro from './screens/editarProf';
import Reserva from './screens/reserva';


const Routes = createAppContainer(
  createSwitchNavigator({
    Login,
    Cadastro,
    CadasAlu,
    CadasPro,
    PerfilAlu,
    PerfilPro,
    EditarAlu,
    EditarPro,
    Reserva
  })
);
export default Routes;

/* APP
import React from 'react'

import Routes from './Routers'

export default function App(){
    return <Routes />
}

*/