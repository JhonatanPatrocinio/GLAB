import React from 'react';

import { View ,StyleSheet} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons'

const Tabs = () => (
    <View styles={styles.container}>
        <Icon name="ios-contact" size={16} style={styles.icon, styles.active} />
        <Icon name="ios-create" size={16} style={styles.icon} />
        <Icon name="ios-search" size={16} style={styles.icon} />
        <Icon name="ios-exit" size={16} style={styles.icon} />
    </View>
);

const styles = StyleSheet.create({
    container:{
        backgroundColor: "#BABACA",
        height: 50,
        paddingHorizontal: 15,
        borderTopWidth: 1,
        borderColor: "#FFFFFF",
        flexDirection: 'row',
        justifyContent: 'space-around',
        alignItems: 'center',
    },
    icon: {
       color: "#C0C0C0"
    },
    active:{
        color: '#F0C0C0'
    }
})

export default Tabs;