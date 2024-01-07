/* 
-----------------
Reference of layout for navigation and initial design: https://www.youtube.com/watch?v=AnjyzruZ36E&ab_channel=Indently
-----------------
*/

import * as React from 'react';

import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import { View, StyleSheet} from 'react-native';

// Screens
import ReviewsScreen from './screens/ReviewsScreen';
import RecommendationsScreen from './screens/RecommendationsScreen';
import LocationScreen from './screens/LocationScreen';
import SearchScreen from './screens/SearchScreen';
import SettingsScreen from './screens/SettingsScreen';

// import { Ionicons } from '@expo/vector-icons';
import Ionicons from '@expo/vector-icons/Ionicons';
import { Entypo } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';
import { MaterialIcons } from '@expo/vector-icons';

// Screen names
const reviewsName = 'Reviews';
const recommendationsName = 'Recommendations';
const locationName = 'Location';
const searchName = 'Search';
const settingsName = 'Settings';

const Tab = createBottomTabNavigator();

export default function MainContainer() {
    return (
        
        // <View style={styles.container}>
        
            <Tab.Navigator
                initialRouteName={locationName}
                screenOptions={({route}) => ({
                    tabBarIcon: ({color, size}) => {
                        let iconName;
                        let routeName = route.name;

                        // Provide the different icons for the different screens
                        if (routeName === reviewsName) {
                            iconName = 'rate-review';
                            return <MaterialIcons name={iconName} size={size} color={color} />;

                        } else if (routeName === recommendationsName) {
                            iconName = 'new';
                            return <Entypo name={iconName} size={size} color={color} />;

                        } else if (routeName === locationName) {
                            iconName = 'location';
                            return <Entypo name={iconName} size={size} color={color} />;

                        } else if (routeName === searchName) {
                            iconName = 'search';
                            return <FontAwesome name={iconName} size={size} color={color} />;

                        } else if (routeName === settingsName) {
                            iconName = 'settings';
                            return <Ionicons name={iconName} size={size} color={color} />;
                        }
                    },
                    tabBarActiveTintColor: 'black',
                    // tabBarInactiveBackgroundColor: 'lightgray',
                    tabBarShowLabel: false,
                    headerShown: false,
                    // style: {
                    //     position: 'absolute',
                    //     alignItems: 'center',
                    //     bottom: 60,
                    //     flexDirection: 'row',
                    //     backgroundColor: '#eee',
                    //     width: '90%',
                    //     justifyContent: 'space-evenly',
                    //     borderRadius: 40,
                    //     backgroundColor: 'black'
                    // }
                })}>
                    <Tab.Screen name={reviewsName} component={ReviewsScreen} />
                    <Tab.Screen name={recommendationsName} component={RecommendationsScreen} />
                    <Tab.Screen name={locationName} component={LocationScreen} />
                    <Tab.Screen name={searchName} component={SearchScreen} />
                    <Tab.Screen name={settingsName} component={SettingsScreen} />
            </Tab.Navigator>
        // </View>
    );
}

const styles = StyleSheet.create({
    container: {
        ...StyleSheet.absoluteFillObject,
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'center',
    },
});