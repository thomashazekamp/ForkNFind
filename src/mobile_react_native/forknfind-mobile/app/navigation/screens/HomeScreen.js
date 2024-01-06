import * as React from 'react';
import { View, Text, StyleSheet, Pressable } from 'react-native';
import { SafeAreaView } from 'react-native';

export default function HomeScreen({ navigation }) {
    return (
        <SafeAreaView style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Text
                onPress={() => alert('This is the home screen!')}
                style= {{ fontSize: 26, fontWeight: 'bold' }}>Home Screen</Text>
        </SafeAreaView>
    );
}