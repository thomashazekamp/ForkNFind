import 'react-native-gesture-handler';
// import { StyleSheet, View, Text, StatusBar, Pressable } from 'react-native';
// import React from 'react';

// import Ionicons from '@expo/vector-icons/Ionicons';
// import { Entypo } from '@expo/vector-icons';
// import { FontAwesome } from '@expo/vector-icons';
// import { MaterialIcons } from '@expo/vector-icons';
// import MapView, { Marker } from 'react-native-maps';

// // Custom components
// // import NavigationBar from './components/NavigationBar';

// /*
//     References: Nav bar design & logic - https://www.youtube.com/watch?v=g14lCxkasWc&ab_channel=Indently
// */

// export default class Home extends React.Component {

//     state = {
//         screenText: 'Press a button!'
//     }

//     changeText = (text) => {
//         console.log(text + ' has been pressed');
//         this.setState({ 
//             screenText: text 
//         });
//     }

//     render() {
//         return (
//             <View style={styles.container}>
//                 <MapView
//                     style={styles.map}
//                     initialRegion={{
//                         latitude: 37.7749,
//                         longitude: -122.4194,
//                         latitudeDelta: 0.0922,
//                         longitudeDelta: 0.0421,
//                 }}
//                 >
//                     <Marker
//                         coordinate={{
//                         latitude: 37.7749,
//                         longitude: -122.4194,
//                         }}
//                         title="Your Location"
//                         description="You are here"
//                     />
//                 </MapView>

//                 <View style={styles.NavContainer}>
//                     <View style={styles.NavBar}>

//                         <Pressable onPress={() => this.changeText('Reviews')} style={styles.IconBehaviour}>
//                         <MaterialIcons name="rate-review" size={24} color="black" />
//                         </Pressable>

//                         <Pressable onPress={() => this.changeText('Recomendations')} style={styles.IconBehaviour}>
//                         <Entypo name="new" size={24} color="black" />
//                         </Pressable>

//                         <Pressable onPress={() => this.changeText('Location')} style={styles.IconBehaviour}>
//                         <Entypo name="location" size={24} color="black" />
//                         </Pressable>

//                         <Pressable onPress={() => this.changeText('Search')} style={styles.IconBehaviour}>
//                         <FontAwesome name="search" size={24} color="black" />
//                         </Pressable>

//                         <Pressable onPress={() => this.changeText('Settings')} style={styles.IconBehaviour}>
//                         <Ionicons name="settings" size={24} color="black" />
//                         </Pressable>

//                     </View>
//                 </View>
//                 {/* <NavigationBar /> */}
//             </View>
//   );
// };
// }

// const styles = StyleSheet.create({
//     container: {
//         ...StyleSheet.absoluteFillObject,
//         flex: 1,
//         justifyContent: 'flex-end',
//         alignItems: 'center',
//     },
//     map: {
//         ...StyleSheet.absoluteFillObject,
//     },
//     NavContainer: {
//         position: 'absolute',
//         alignItems: 'center',
//         bottom: 40,
//     },

//     NavBar: {
//         flexDirection: 'row',
//         backgroundColor: '#eee',
//         width: '90%',
//         justifyContent: 'space-evenly',
//         borderRadius: 40,
//     },

//     IconBehaviour: {
//         padding: 14,
//     }
//   });

import * as React from 'react';
import MainContainer from './navigation/MainContainer';

import { NavigationContainer } from '@react-navigation/native';

function App() {
    return (
        // <NavigationContainer>
            <MainContainer />
        // </NavigationContainer>
    );
}

export default App;