
import React, { useState, useEffect, Component } from 'react';
import { View, AsyncStorage, Text, StyleSheet, ImageBackground, Image, Platform, TextInput, Dimensions, TouchableOpacity, KeyboardAvoidingView } from 'react-native';

import api from '../src/services/api'


import { ScrollView } from 'react-native-gesture-handler';

import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'
import Icon from 'react-native-vector-icons/Ionicons'


const { width: WIDTH } = Dimensions.get('window')


export default function TelaLogin({ navigation }) {
  //variaveis que armazena os dados
 
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  

  //Para continuar logado ao atualizar a pagina
  /*
   useEffect(()=>{
     AsyncStorage.getItem('user').then(user =>{
       if(user) {
         //Alterar esse dados quando definir a forma de diferenciar usuarios
         navigation.navigate('PerfilPro');
       }
     })
   },[]);
 */

  //Armazenar valores dos inputs
  async function handleSubmit() {
    //Conexao com api para salvar logins e senhas
    /*
     const response = await api.post('/sessions',{
       email
     })
   
     const { _id } = response.data;
   
     console.log(_id);
   
     */
    //mostrar no log
    console.log(email);
    console.log(senha);

    //await AsyncStorage.setItem('user', _id);
    //await AsyncStorage.setItem('senha', senha)

    //alteraçao de telas
    navigation.navigate('PerfilPro');
  }

  async function handleSubmit2() {
    navigation.navigate('Cadastro');
  }









  return (
    <ImageBackground source={bgImage} style={styles.backgroundContainer}>

      <KeyboardAvoidingView enabled={Platform.OS == 'ios'} behavior='padding'>
        <ScrollView>
          <View><Text style={styles.logoTextU}>Universidade Federal do Acre</Text></View>
          <View style={styles.logoContainer}>
            <Image source={logo} />
            <Text style={styles.logoText}>Gerenciado de Laboratorios Acessivel Brasileiro</Text>

          </View>

          <View style={styles.inputContainer}>
            <Icon name={'ios-person'} size={28} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
            <TextInput
              style={styles.input}
              placeholder={'Usuario'}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
              keyboardType="email-address"
              autoCapitalize="none"
              autoCorrect={false}
              //variaves dos dados Email
              value={email}
              onChangeText={setEmail}
            />
          </View>

          <View style={styles.inputContainer}>
            <Icon name={'ios-lock'} size={28} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
            <TextInput
              style={styles.input}
              placeholder={'Senha'}
              secureTextEntry={true}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
              //variaves dos dados Senha
              value={senha}
              onChangeText={setSenha}
            />
          </View>

          <TouchableOpacity onPress={handleSubmit} style={styles.btnLogin}>
            <Text style={styles.text}>Login</Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={handleSubmit2} style={styles.btnLogin} >
            <Text style={styles.text}>Cadastro</Text>
          </TouchableOpacity>

          <Text style={styles.rodape}>Desenvolvido por Tiago Prata & Jhonatan Patrocinio</Text>
        </ScrollView>
      </KeyboardAvoidingView>

    </ImageBackground>
  );

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
    fontSize: 25,
    fontWeight: '500',
    marginTop: 1,
    textAlign: 'center'

  },
  logoTextU: {
    color: '#ffffff',
    fontSize: 20,
    fontWeight: '500',
    marginTop: 30,
    textAlign: 'center'

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
    backgroundColor: 'rgba(255, 255, 255, 0.35)',
    color: 'rgba(255, 255, 255, 0.7)',
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
    marginHorizontal: 25,
    marginTop: 20,
    paddingLeft: 45


  },
  text: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: 16,
    top: 8,
    marginEnd: 30,
    textAlign: 'center'

  },
  rodape: {
    color: '#ffffff',
    marginTop: 30,
    textAlign: 'center',
    fontSize: 10
  }
});
/*
class MostraSenha extends Component {

 

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

  render(){
    
    return(
                 <View style={styles.inputContainer}>
                    <Icon name={'ios-lock'} size={28} color={'rgba(255, 255, 255, 0.7)'}
                      style={styles.inputIcon} />
                    <TextInput
                      style={styles.input}
                      placeholder={'Senha'}
                      secureTextEntry={this.state.showPass}
                      placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                      underlineColorAndroid='transparent'
                      variaves dos dados Senha
                      value={senha}
                      onChangeText={setSenha}
                    />
      
                    <TouchableOpacity style={styles.btnEye}
                      onPress={this.showPass.bind(this)}>
                      <Icon name={this.state.press == false ? 'ios-eye' : 'ios-eye-off'}
                        size={26} color={'rgba(255, 255, 255, 0.7)'}
                      />
                    </TouchableOpacity>
                  </View>
    );
  }

}


/*
<View style={styles.inputContainer}>
            <Icon name={'ios-lock'} size={28} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
            <TextInput
              style={styles.input}
              placeholder={'Senha'}
              secureTextEntry={true}
              placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
              underlineColorAndroid='transparent'
              //variaves dos dados Senha
              value={senha}
              onChangeText={setSenha}
            />
          </View>
          */