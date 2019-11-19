import React from 'react'
import { StyleSheet, Text, View} from 'react-native'
import {createStackNavigation} from 'react-native'

export default class LoginScreen extends React.Component{
  render(){
    return(
      <view style={StyleSheet.container}>
        <text>OPen up App.js</text>
      </view>
    )
  }
}

export default createStackNavigation({
  Login:{
    screen:LoginScreen
  }
})
  


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});