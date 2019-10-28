import React, { Component } from 'react';
import { View, Text, StyleSheet, ImageBackground, Image, TextInput, Dimensions, TouchableOpacity, Picker, KeyboardAvoidingView, Alert} from 'react-native';


import bgImage from './src/img/background.jpg'
import logo from './src/img/Glab.png'

import { ScrollView } from 'react-native-gesture-handler';

const { width: WIDTH } = Dimensions.get('window')

export default class CadastroProf extends Component {

  state = {
    selecionado: ''
  }


  render() {
    return (

      <ImageBackground source={bgImage} style={styles.backgroundContainer}>
        <KeyboardAvoidingView behavior='padding'>
        <ScrollView style={{ flex: 1 }} >
        
          <View style={styles.backgroundContainer}>
            <View><Text style={styles.logoText}>Cadastro Professor</Text></View>

            <View style={styles.logoContainer}>
              <Image source={logo} />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Matricula</Text>
              <TextInput
                style={styles.input}
                //placeholder={''}
                placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                underlineColorAndroid='transparent'
              />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Centro</Text>
              <Picker
                style={styles.pickerComponete}
                selectedValue={this.state.selecionado}
                onValueChange={
                  (itemValor, itemIndex) =>
                    this.setState({
                      selecionado: itemValor
                    })
                }>
                <Picker.Item label="..." value="" />
                <Picker.Item label="CCET" value="CCET" />
                <Picker.Item label="CJSA" value="CJSA" />

              </Picker>
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Nome</Text>
              <TextInput
                style={styles.input}
                //placeholder={''}
                placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                underlineColorAndroid='transparent'
              />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Login</Text>
              <TextInput
                style={styles.input}
                //placeholder={''}
                placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                underlineColorAndroid='transparent'
              />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Senha</Text>
              <TextInput
                style={styles.input}
                //placeholder={''}
                secureTextEntry={true}
                placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                underlineColorAndroid='transparent'
              />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Confirmar Senha</Text>
              <TextInput
                style={styles.input}
                //placeholder={''}
                secureTextEntry={true}
                placeholderTextColor={'rgba(255, 255, 255, 0.7)'}
                underlineColorAndroid='transparent'
              />
            </View>

            <TouchableOpacity style={styles.btnLogin}
            onPress={() => Alert.alert(
              'Confirmação',
              'Tem certeza que os dados inseridos estão corretos?',
              [
                {
                  text: 'Não',
                  onPress: () => console.log('Cancel Pressed'),
                  style: 'Não',
                },
                { text: 'Sim', onPress: () => console.log('OK Pressed') },
              ],
              { cancelable: false },
            )}
            >
              <Text style={styles.text}>Cadastrar</Text>
            </TouchableOpacity>

          </View>

          

        </ScrollView>
        </KeyboardAvoidingView>
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
    fontSize: 25,
    fontWeight: '500',
    marginTop: 20

  },
  titulos: {
    color: '#ffffff',
    fontSize: 20,
    fontWeight: '500',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 2,
    marginEnd: 10,
    paddingLeft: 40

  },
  inputContainer: {
    marginTop: 10
  },
  input: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 25,
    fontSize: 16,
    paddingLeft: 20,
    backgroundColor: 'rgba(255, 255, 255, 0.5)',
    color: 'rgba(0, 0, 0, 1)',
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
    marginEnd: 30
  },
  text: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: 16,
    textAlign: 'center'
  },
  rodape: {
    color: '#ffffff',
    marginTop: 30,
    justifyContent: 'center'
  },
  pickerComponete: {
    width: WIDTH - 55,
    borderRadius: 25,
    fontSize: 16,
    backgroundColor: 'rgba(255, 255, 255, 0.5)',
    color: 'rgba(255, 255, 255, 1)',
    marginHorizontal: 25

  }
});