import React from "react"
import {View, Text} from "react-native"

export default class Rodape extends React.Component{
    render(){
        return(
            <View
            style={{alignItems: "center", margin: 40}}
            >
                
                
                <Text style={{color: "#ffffff", alignItems: "center"}}>Desenvolvido por Tiago Prata e Jhonatan Patrocinio</Text>
                <Text style={{color: "#ffffff", margin:5, alignItems: "center"}}>Orientado por Daricelio Soares</Text>
            </View>

        )
    }
}