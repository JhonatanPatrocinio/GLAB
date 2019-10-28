import React, { Component } from 'react';
import { View, Text, StyleSheet, ImageBackground, Image, Dimensions, TouchableOpacity, Alert } from 'react-native';


import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'


import {Calendar} from 'react-native-calendars'
import {LocaleConfig} from 'react-native-calendars';
import { ScrollView } from 'react-native-gesture-handler';

LocaleConfig.locales['br'] = {
  monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
  monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dec'],
  dayNames: ['Domingo','Segunda','terça','Quarta','Quinta','Sexta','Sabado'],
  dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sab'],
  today: 'Hoje\'Hoj'
};
LocaleConfig.defaultLocale = 'br';

const { width: WIDTH } = Dimensions.get('window')

export default class Reserva extends Component {

  render() {
    return (

      <ImageBackground source={bgImage} style={styles.backgroundContainer}>
        <ScrollView style={{ flex: 1 }}>
        <View style={styles.backgroundContainer}>

          <View><Text style={styles.logoText}>Reservas</Text></View>

          <View style={styles.inputContainer}>
            <Text style={styles.titulos}>Selecione a data da reserva</Text>
          </View>

          <View style={styles.logoContainer}>
            <Image source={logo} />
          </View>

          <View style={styles.inputContainer}>
              <Text style={styles.titulos}>Espaço</Text>
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
                <Picker.Item label="Laboratorio 1" value="lab1" />
                <Picker.Item label="Espaço de conversa" value="ep1" />

              </Picker>
            </View>

          <Calendar
          style={{borderWidth: 2,
          borderColor: 'black',
          height: 50,
          width: WIDTH - 50,
          borderRadius: 25,
          marginEnd:30
          }}
          />

          


        </View>
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