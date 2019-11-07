import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet, ImageBackground, Image, Dimensions, TouchableOpacity, Alert, Button } from 'react-native';


import bgImage from '../src/img/background.jpg'
import logo from '../src/img/Glab.png'
import Icon from 'react-native-vector-icons/Ionicons'



import { ScrollView } from 'react-native-gesture-handler';
import DateTimePicker from "react-native-modal-datetime-picker";


const { width: WIDTH } = Dimensions.get('window')


export default function Reserva({ navigation }) {



  async function tela2() {
    navigation.navigate('PerfilPro');
  }

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

          <Selecionador />

          <SelecionaData />

          <TouchableOpacity onPress={tela2} style={styles.btnLogin} >
            <Text style={styles.text}>Voltar</Text>
            <Icon name={'ios-undo'} size={22} color={'rgba(255, 255, 255, 0.7)'}
              style={styles.inputIcon} />
          </TouchableOpacity>

          <TouchableOpacity onPress={tela2} style={styles.btnVreserva} >
            <Text style={styles.text}>Efetuar Reserva</Text>
            <Icon name={'ios-save'} size={22} color={'rgba(255, 255, 255, 0.7)'}
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
  inputIcon2: {
    position: 'absolute',
    top: 30,
    left: 62
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

    right:35,
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
    right: -35,
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

  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF'
  },
  button: {
    width: 250,
    height: 50,
    borderRadius: 25,
    justifyContent: 'center',
    marginTop: 15
  },
  textData: {
    fontSize: 18,
    color: 'white',
    textAlign: 'center'
  }
});


class Selecionador extends Component {

  state = {
    selecionado: ''
  }

  render() {


    return (

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
          <Picker.Item label="Laboratorio 2" value="lab2" />

        </Picker>
      </View>


    );
  }
}


class SelecionaData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isDateTimePickerVisible: false
    };
  }

  showDateTimePicker = () => {
    this.setState({ isDateTimePickerVisible: true });
  };

  hideDateTimePicker = () => {
    this.setState({ isDateTimePickerVisible: false });
  };

  handleDatePicked = date => {
    console.log("A date has been picked: ", date);
    this.hideDateTimePicker();
  };

  render() {
    return (
      <>

        <TouchableOpacity style={styles.button} onPress={this.showDateTimePicker}>
          <Text style={styles.textData} >Selecionar Data e Horario</Text>
        </TouchableOpacity>

        <DateTimePicker
          isVisible={this.state.isDateTimePickerVisible}
          onConfirm={this.handleDatePicked}
          onCancel={this.hideDateTimePicker}
          mode={'datetime'}
          titleIOS={'Selecione data e horario'}
          is24Hour={true}
          locale="pt_BR"


        />


      </>


    );
  }
}

/*

<TouchableOpacity onPress={tela3} style={styles.btnReserva} >
<Text style={styles.text}>Voltar</Text>
<Icon name={'ios-create'} size={22} color={'rgba(255, 255, 255, 0.7)'}
  style={styles.inputIcon} />
</TouchableOpacity>

<TouchableOpacity onPress={() => Alert.alert(
'Confirmação',
'Tem certeza que deseja efetuar a reserva?',
[
  {
    text: 'Não',
    onPress: () => console.log('Cancel Pressed'),
    style: 'Não',
  },
  { text: 'Sim', onPress: () => navigation.navigate('PerfilPro') },
],
{ cancelable: false },
)}
style={styles.btnVreserva} >
<Text style={styles.text}>Efetuar Reserva</Text>
<Icon name={'ios-search'} size={22} color={'rgba(255, 255, 255, 0.7)'}
  style={styles.inputIcon} />
</TouchableOpacity>
*/