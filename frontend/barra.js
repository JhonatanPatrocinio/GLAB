//This is an example code for NavigationDrawer//
import React, { Component } from 'react';
//import react in our code.
import { View, Image, TouchableOpacity } from 'react-native';
// import all basic components
import {createAppContainer} from 'react-navigation';
import {createDrawerNavigator} from 'react-navigation-drawer';
import {createStackNavigator} from 'react-navigation-stack';
import Screen1 from './screens/perfilProf';
import Screen2 from './screens/editarProf';
import Screen3 from './screens/telaLogin';

import icone from '../Glab/src/img/drawer.png';
 
class NavigationDrawerStructure extends Component {
  //Structure for the navigatin Drawer
  toggleDrawer = () => {
    //Props to open/close the drawer
    this.props.navigationProps.toggleDrawer();
  };
  render() {
    return (
      <View style={{ flexDirection: 'row' }}>
        <TouchableOpacity onPress={this.toggleDrawer.bind(this)}>
          {/*Donute Button Image */}
          <Image
            source={icone}
            style={{ width: 25, height: 25, marginLeft: 5 }}
          />
        </TouchableOpacity>
      </View>
    );
  }
}
  
const FirstActivity_StackNavigator = createStackNavigator({
    //All the screen from the Screen1 will be indexed here
    First: {
      screen: Screen1,
      navigationOptions: ({ navigation }) => ({
        title: 'Perfil',
        headerLeft: <NavigationDrawerStructure navigationProps={navigation} />,
        headerStyle: {
          backgroundColor: 'rgba(255, 255, 255, 0.7)',
        },
        headerTintColor: '#fff',
      }),
    },
  });
  
const Screen2_StackNavigator = createStackNavigator({
    //All the screen from the Screen2 will be indexed here
    Second: {
      screen: Screen2,
      navigationOptions: ({ navigation }) => ({
        title: 'Editar informações',
        headerLeft: <NavigationDrawerStructure navigationProps={navigation} />,
        headerStyle: {
          backgroundColor: 'rgba(255, 255, 255, 0.7)',
        },
        headerTintColor: '#fff',
      }),
    },
  });
   
  const Screen3_StackNavigator = createStackNavigator({
    //All the screen from the Screen3 will be indexed here
    Third: {
      screen: Screen3,
      navigationOptions: ({ navigation }) => ({
        title: 'Sair',
        headerLeft: <NavigationDrawerStructure navigationProps={navigation} />,
        headerStyle: {
          backgroundColor: 'rgba(255, 255, 255, 0.7)',
        },
        headerTintColor: '#fff',
      }),
    },
  });
   
  const DrawerNavigatorExample = createDrawerNavigator({
    //Drawer Optons and indexing
    Screen1: {
      //Title
      screen: FirstActivity_StackNavigator,
      navigationOptions: {
        drawerLabel: 'Perfil',
      },
    },
    Screen2: {
      //Title
      screen: Screen2_StackNavigator,
      navigationOptions: {
        drawerLabel: 'Editar informações',
      },
    },
    Screen3: {
      //Title
      screen: Screen3_StackNavigator,
      navigationOptions: {
        drawerLabel: 'Sair',
      },
    },
  });
   
  export default createAppContainer(DrawerNavigatorExample);  