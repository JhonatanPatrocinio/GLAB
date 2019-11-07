import React, { Component } from 'react';
import { View, Text, StyleSheet, ImageBackground, Image, Dimensions, TouchableOpacity, Alert } from 'react-native';


import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'
import Icon from 'react-native-vector-icons/Ionicons'

import { Calendar } from 'react-native-calendars'
import { LocaleConfig } from 'react-native-calendars';
import { ScrollView } from 'react-native-gesture-handler';

LocaleConfig.locales['br'] = {
  monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
  monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dec'],
  dayNames: ['Domingo', 'Segunda', 'terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'],
  dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
  today: 'Hoje\'Hoj'
};
LocaleConfig.defaultLocale = 'br';

const { width: WIDTH } = Dimensions.get('window')

export default function PerfilAlun({navigation}) {

  async function tela1() {
    navigation.navigate('Login');
}
async function tela2() {
    navigation.navigate('EditarAlu');
}


    return (

      <ImageBackground source={bgImage} style={styles.backgroundContainer}>
        <ScrollView style={{ flex: 1 }}>
          <View style={styles.TodoContainer}>

            <View><Text style={styles.logoText}>ALUNO</Text></View>

            <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Nome do Aluno</Text>
            </View>

            <View style={styles.logoContainer}>
              <Image source={logo} />
            </View>

            <Calendar
              style={{
                borderWidth: 2,
                borderColor: 'black',
                height: 325,
                width: WIDTH - 50,
                borderRadius: 25,
                marginEnd: 30,
                left: 15
              }}
            />

            <TouchableOpacity onPress={tela2} style={styles.btnLogin} >
              <Text style={styles.text}>Editar Perfil</Text>
              <Icon name={'ios-contact'} size={22} color={'rgba(255, 255, 255, 0.7)'}
                style={styles.inputIcon} />
            </TouchableOpacity>


            <TouchableOpacity style={styles.btnVreserva} >
              <Text style={styles.text}>Verificar reservas</Text>
              <Icon name={'ios-search'} size={22} color={'rgba(255, 255, 255, 0.7)'}
                style={styles.inputIcon} />
            </TouchableOpacity>

            <TouchableOpacity onPress={tela1} style={styles.btnSair} >
              <Text style={styles.text}>Sair</Text>
              <Icon name={'ios-exit'} size={22} color={'rgba(255, 255, 255, 0.7)'}
                style={styles.inputIcon} />
            </TouchableOpacity>


          </View>
        </ScrollView>
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
  TodoContainer: {


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
      top: 30,
      left: 22
  },
  btnEye: {
      position: 'absolute',
      top: 10,
      right: 37
  },
  btnLogin: {
      width: 60,
      height: 60,
      borderRadius: 20,
      backgroundColor: '#432577',
      justifyContent: 'center',
      marginTop: 10,
     
      right: 110,
      end: 30
  },
  btnReserva: {
      width: 60,
      height: 60,
      borderRadius: 20,
      backgroundColor: '#432577',
      justifyContent: 'center',
      marginTop: -60,
      right: 35,
      end: 30
  },
  btnVreserva: {
      width: 60,
      height: 60,
      borderRadius: 20,
      backgroundColor: '#432577',
      justifyContent: 'center',
      marginTop: -60,
      right: 0,
      end: 30
  },
  btnSair: {
      width: 60,
      height: 60,
      borderRadius: 20,
      backgroundColor: '#432577',
      justifyContent: 'center',
      marginTop: -60,
      right: -110,
      end: 30
  },
  text: {
      color: 'rgba(255, 255, 255, 0.7)',
      fontSize: 10,
      textAlign: 'center',
      fontWeight: 'bold',
      left: 1,
      top: -13
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
