import * as React from 'react';
import { View, Text, StyleSheet, Pressable } from 'react-native';
import MapView, { Marker } from 'react-native-maps';

export default function SettingsScreen({ navigation }) {
    return (
        <View style={styles.container}>
                <MapView
                    style={styles.map}
                    initialRegion={{
                        latitude: 37.7749,
                        longitude: -122.4194,
                        latitudeDelta: 0.0922,
                        longitudeDelta: 0.0421,
                }}
                >
                    <Marker
                        coordinate={{
                        latitude: 37.7749,
                        longitude: -122.4194,
                        }}
                        title="Your Location"
                        description="You are here"
                    />
                </MapView>
            {/* <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
                <Text
                    onPress={() => navigation.navigate('Home')}
                    style= {{ fontSize: 26, fontWeight: 'bold' }}>Details Screen</Text>
            </View> */}
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        ...StyleSheet.absoluteFillObject,
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'center',
    },
    map: {
        ...StyleSheet.absoluteFillObject,
    }
});