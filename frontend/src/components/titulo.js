import React from "react"
import {View,Text} from "react-native"

export default class Titulo extends React.Component{
    render(){
        return(
            <View
            style={{alignItems: "center", margin: 20}}
            >
                <Text style={{fontSize:50, color: "#66dbfc"}}>GLAB</Text>
               
                
            </View>
        )
    }
}