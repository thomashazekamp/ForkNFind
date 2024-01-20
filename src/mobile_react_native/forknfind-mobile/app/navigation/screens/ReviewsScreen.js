import * as React from 'react';
import { View, Text, StyleSheet, Pressable, SafeAreaView } from 'react-native';

export default function ReviewsScreen({ navigation }) {
    return (
        <SafeAreaView style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Text
                style= {{ fontSize: 26, fontWeight: 'bold' }}>Reviews Screen</Text>
        </SafeAreaView>
    );
}