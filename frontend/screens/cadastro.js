import React from 'react';
import { View, Text, StyleSheet, ImageBackground, Image, Dimensions, TouchableOpacity, Alert } from 'react-native';


import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'
import Icon from 'react-native-vector-icons/Ionicons'



const { width: WIDTH } = Dimensions.get('window')

export default function Cadastro({navigation}) {


  
    return (

      <ImageBackground source={bgImage} style={styles.backgroundContainer}>

        <View style={styles.backgroundContainer}>

          <View><Text style={styles.logoText}>Cadastro</Text></View>

          <View style={styles.logoContainer}>
            <Image source={logo} />
          </View>

          <View style={styles.inputContainer}>
            <Text style={styles.titulos}>Selecione seu perfil</Text>
          </View>



          <TouchableOpacity style={styles.btnLogin}
             onPress={() => Alert.alert(
              'Confirmação',
              'Tem certeza que selecionou a opção certa?',
              [
                {
                  text: 'Não',
                  onPress: () => console.log('Cancel Pressed'),
                  style: 'Não',
                },
                { text: 'Sim', onPress: () => navigation.navigate('CadasAlu') },
              ],
              { cancelable: false },
            )}
          >
            <Icon name={'ios-person'} size={60} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
            <Text style={styles.text}>Aluno</Text>

          </TouchableOpacity>


          <TouchableOpacity style={styles.btnLogin}
            onPress={() => Alert.alert(
              'Confirmação',
              'Tem certeza que selecionou a opção certa?',
              [
                {
                  text: 'Não',
                  onPress: () => console.log('Cancel Pressed'),
                  style: 'Não',
                },
                { text: 'Sim', onPress: () => navigation.navigate('CadasPro')  },
              ],
              { cancelable: false },
            )}
          >
            <Icon name={'ios-school'} size={60} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
            <Text style={styles.text}>        Professor</Text>

          </TouchableOpacity>


        </View>

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
    marginTop: 20

  },
  titulos: {
    color: '#ffffff',
    fontSize: 20,
    fontWeight: '500',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 2,
    marginEnd: 10

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
    top: 20,
    left: 27
  },
  btnEye: {
    position: 'absolute',
    top: 8,
    right: 37
  },
  btnLogin: {
    width: WIDTH - 100,
    height: 100,
    borderRadius: 25,
    backgroundColor: '#432577',
    justifyContent: 'center',
    marginTop: 20
  },
  text: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: 16,
    textAlign: 'center',
    left: 10
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