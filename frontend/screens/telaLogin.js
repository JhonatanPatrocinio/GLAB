import React, { Component } from 'react';
import { View, Text, StyleSheet, ImageBackground, Image, TextInput, Dimensions, TouchableOpacity, KeyboardAvoidingView } from 'react-native';

import { ScrollView } from 'react-native-gesture-handler';

import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'
import Icon from 'react-native-vector-icons/Ionicons'


const { width: WIDTH } = Dimensions.get('window')

export default class TelaLogin extends Component {
  constructor() {
    super()
    this.state = {
      showPass: true,
      press: false
    }
  }

  showPass = () => {
    if (this.state.press == false) {
      this.setState({ showPass: false, press: true })
    } else {
      this.setState({ showPass: true, press: false })
    }
  }

  render() {
    return (
      <ImageBackground source={bgImage} style={styles.backgroundContainer}>
        <ScrollView style={{ flex: 1 }}>
        <KeyboardAvoidingView behavior='padding'>

        <View><Text style={styles.logoText}>Universidade Federal do Acre</Text></View>
        <View style={styles.logoContainer}>
          <Image source={logo} />
          <Text style={styles.logoText}>Gerenciado de Laboratorios Acessivel Brasileiro</Text>

        </View>

        <View style={styles.inputContainer}>
          <Icon name={'ios-person'} size={28} color={'rgba(255, 255, 255, 0.7)'}
            style={styles.inputIcon} />
          <TextInput
            style={styles.input}
            placeholder={'Usuario'}
            placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
            underlineColorAndroid='transparent'
          />
        </View>

        <View style={styles.inputContainer}>
          <Icon name={'ios-lock'} size={28} color={'rgba(255, 255, 255, 0.7)'}
            style={styles.inputIcon} />
          <TextInput
            style={styles.input}
            placeholder={'Senha'}
            secureTextEntry={this.state.showPass}
            placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
            underlineColorAndroid='transparent'
          />

          <TouchableOpacity style={styles.btnEye}
            onPress={this.showPass.bind(this)}>
            <Icon name={this.state.press == false ? 'ios-eye' : 'ios-eye-off'}
              size={26} color={'rgba(255, 255, 255, 0.7)'}
            />
          </TouchableOpacity>
        </View>

        <TouchableOpacity style={styles.btnLogin}>
          <Text style={styles.text}>Login</Text>
        </TouchableOpacity> 

        <TouchableOpacity style={styles.btnLogin} 
        onPress={
          
        }>
          <Text style={styles.text}>Cadastro</Text>
        </TouchableOpacity>

        <Text style={styles.rodape}>Desenvolvido por Tiago Prata & Jhonatan Patrocinio</Text>
        </KeyboardAvoidingView>
        </ScrollView>
      </ImageBackground>
    );
  }
}




const styles = StyleSheet.create({
  backgroundContainer: {
    flex: 1,
    width: null,
    height: null,
    justifyContent: 'center',
    alignItems: 'center'

  },
  logoContainer: {
    alignItems: 'center',
    marginBottom: 2

  },
  logoText: {
    color: '#ffffff',
    fontSize: 20,
    fontWeight: '500',
    marginTop: 1,

  },
  inputContainer: {
    marginTop: 10
  },
  input: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 25,
    fontSize: 16,
    paddingLeft: 45,
    backgroundColor: 'rgba(255, 255, 255, 0.35)',
    color: 'rgba(255, 255, 255, 0.7)',
    marginHorizontal: 25

  },
  inputIcon: {
    position: 'absolute',
    top: 8,
    left: 37
  },
  btnEye: {
    position: 'absolute',
    top: 8,
    right: 37
  },
  btnLogin: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 25,
    backgroundColor: '#432577',
    justifyContent: 'center',
    marginTop: 20,
    left: 37
  },
  text: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: 16,
    textAlign: 'center',
    marginEnd: 30
  },
  rodape: {
    color: '#ffffff',
    marginTop: 30,
    justifyContent: 'center'
  }
});