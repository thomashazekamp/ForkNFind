/* 
-----------------
Reference of layout for navigation and initial design: https://www.youtube.com/watch?v=AnjyzruZ36E&ab_channel=Indently
-----------------
*/

import * as React from 'react';
// import { View, Text, StyleSheet, Pressable } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

// Screens
import HomeScreen from './screens/HomeScreen';
import DetailsScreen from './screens/DetailsScreen';
import SettingsScreen from './screens/SettingsScreen';

import { Ionicons } from '@expo/vector-icons';

// Screen names
const homeName = 'Home';
const detailsName = 'Details';
const settingsName = 'Settings';

const Tab = createBottomTabNavigator();

export default function MainContainer() {
    return (
        <NavigationContainer independent={true}>
            <Tab.Navigator
                initialRouteName={homeName}
                screenOptions={({route}) => ({
                    tabBarIcon: ({focused, color, size}) => {
                        let iconName;
                        let routeName = route.name;

                        if (routeName === homeName) {
                            iconName = focused ? 'home' : 'home-outline';
                        } else if (routeName === detailsName) {
                            iconName = focused ? 'list' : 'list-outline';
                        } else if (routeName === settingsName) {
                            iconName = focused ? 'settings' : 'settings-outline';
                        }

                        return <Ionicons name={iconName} size={size} color={color} />;
                    },
                    headerShown: false,
                })}>

                    <Tab.Screen name={homeName} component={HomeScreen} />
                    <Tab.Screen name={detailsName} component={DetailsScreen} />
                    <Tab.Screen name={settingsName} component={SettingsScreen} />
            </Tab.Navigator>
        </NavigationContainer>
    );
}