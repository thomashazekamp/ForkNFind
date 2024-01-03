import { StyleSheet, View, Text, StatusBar, Pressable } from 'react-native';
import React from 'react';

import Ionicons from '@expo/vector-icons/Ionicons';
import { Entypo } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';
import { MaterialIcons } from '@expo/vector-icons';

/*
    References: Nav bar design & logic - https://www.youtube.com/watch?v=g14lCxkasWc&ab_channel=Indently
*/

export default class Home extends React.Component {

    state = {
        screenText: 'Press a button!'
    }

    changeText = (text) => {
        console.log(text + ' has been pressed');
        this.setState({ 
            screenText: text 
        });
    }

    render() {
        return (
            <View style={styles.container}>
                <View>
                    <Text style={{fontSize:30, color:'white'}}>{this.state.screenText}</Text>
                </View>

                <View style={styles.NavContainer}>
                    <View style={styles.NavBar}>

                    <Pressable onPress={() => this.changeText('Reviews')} style={styles.IconBehaviour}>
                    <MaterialIcons name="rate-review" size={24} color="black" />
                    </Pressable>

                    <Pressable onPress={() => this.changeText('Recomendations')} style={styles.IconBehaviour}>
                    <Entypo name="new" size={24} color="black" />
                    </Pressable>

                    <Pressable onPress={() => this.changeText('Location')} style={styles.IconBehaviour}>
                    <Entypo name="location" size={24} color="black" />
                    </Pressable>

                    <Pressable onPress={() => this.changeText('Search')} style={styles.IconBehaviour}>
                    <FontAwesome name="search" size={24} color="black" />
                    </Pressable>

                    <Pressable onPress={() => this.changeText('Settings')} style={styles.IconBehaviour}>
                    <Ionicons name="settings" size={24} color="black" />
                    </Pressable>

                    </View>

                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: 'black',
        alignItems: 'center',
        justifyContent:'center',
    },

    NavContainer: {
        position: 'absolute',
        alignItems: 'center',
        bottom: 20,
    },

    NavBar: {
        flexDirection: 'row',
        backgroundColor: '#eee',
        width: '90%',
        justifyContent: 'space-evenly',
        borderRadius: 40,
    },

    IconBehaviour: {
        padding: 14,
    }
});