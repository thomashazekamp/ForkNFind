/* 
-----------------
Reference of layout for navigation and initial design: https://www.youtube.com/watch?v=AnjyzruZ36E&ab_channel=Indently
-----------------
*/

import React, { useState, useEffect } from 'react';

import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { useNavigation } from '@react-navigation/native';

import { View, StyleSheet} from 'react-native';

// Screens
import ReviewsScreen from './screens/ReviewsScreen';
import RecommendationsScreen from './screens/RecommendationsScreen';
import LocationScreen from './screens/LocationScreen';
import SearchScreen from './screens/SearchScreen';
import SettingsScreen from './screens/SettingsScreen';
import LoginScreen from './screens/LoginScreen';
import CreateAccountScreen from './screens/CreateAccountScreen';

// import { Ionicons } from '@expo/vector-icons';
import Ionicons from '@expo/vector-icons/Ionicons';
import { Entypo } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';
import { MaterialIcons } from '@expo/vector-icons';
import { FontAwesome5 } from '@expo/vector-icons';

// Screen names
const reviewsName = 'Reviews';
const recommendationsName = 'Recommendations';
const locationName = 'Location';
const searchName = 'Search';
const settingsName = 'Settings';
const loginName = "Login";

const Tab = createBottomTabNavigator();

// Global variables for saving username and access token
var username_global = "";
var access_global = "";

// Functional Component MainContainer
export default function MainContainer() {

    // Use state for checking if a user is logged in or not
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    const navigation = useNavigation();

    // useEffect for checking once a user logs in, the page to redirect them too.
    useEffect(() => {
        // Check if isLoggedIn becomes true
        if (isLoggedIn) {
            // Navigate to map screen
            navigation.navigate('Location');
        }
    }, [isLoggedIn]);

    // The navigation and nav bar a user will see when logged in
    const NormalScreen = () => {

        return (
            <Tab.Navigator
                    initialRouteName={locationName}
                    screenOptions={({route}) => ({
                        // Custom nav bar styling
                        tabBarStyle: {backgroundColor: 'black',
                            borderTopWidth: 0,
                            position: 'absolute',
                            bottom: '5%',
                            left: '7.5%',
                            right: '7.5%',
                            height: '7%',
                            borderRadius: 20000,
                            paddingBottom: 0,
                        },
                        tabBarItemStyle: {borderRadius: 100000},
                        tabBarIcon: ({color}) => {
                            let iconName;
                            let routeName = route.name;
    
                            // Provide the different icons for the different screens
                            if (routeName === reviewsName) {
                                iconName = 'rate-review';
                                return <MaterialIcons name={iconName} size={25} color={color}  />;
    
                            } else if (routeName === recommendationsName) {
                                iconName = 'lightbulb';
                                return <FontAwesome5 name={iconName} size={25} color={color} />
    
                            } else if (routeName === locationName) {
                                iconName = 'location';
                                return <Entypo name={iconName} size={25} color={color} />;
    
                            } else if (routeName === searchName) {
                                iconName = 'search';
                                return <FontAwesome name={iconName} size={25} color={color} />;
    
                            } else if (routeName === settingsName) {
                                iconName = 'settings';
                                return <Ionicons name={iconName} size={25} color={color} />;
                            }
                        },
                        tabBarActiveTintColor: 'white',
                        tabBarInactiveTintColor: 'white',
                        tabBarActiveBackgroundColor: '#1C58F2',
                        tabBarShowLabel: false,
                        headerShown: false,
                    })}>
                        <Tab.Screen name={reviewsName} component={ReviewsScreen} />
                        <Tab.Screen name={recommendationsName} component={RecommendationsScreen} />
                        <Tab.Screen name={locationName} component={LocationScreen} />
                        <Tab.Screen name={searchName} component={SearchScreen} />
                        <Tab.Screen name={settingsName}>
                            {(props) => <SettingsScreen {...props} setIsLoggedIn={setIsLoggedIn} />}
                        </Tab.Screen>
                </Tab.Navigator>
        )
    }

    // The screens a user will see when not logged in
    const LoginScreenFunction = () => {

        return (
            <Tab.Navigator
                initialRouteName={loginName}
                // This hides the nav bar
                screenOptions={({route}) => ({
                    tabBarStyle: {backgroundColor: 'black',
                            borderTopWidth: 0,
                            position: 'absolute',
                            bottom: '-50%',
                            left: '7.5%',
                            right: '7.5%',
                            height: '7%',
                            borderRadius: 20000,
                            paddingBottom: 0,
                        },
                    tabBarShowLabel: false,
                    headerShown: false,
                    })}
            >
                <Tab.Screen name="Login">
                    {(props) => <LoginScreen {...props} setIsLoggedIn={setIsLoggedIn} />}
                </Tab.Screen>
                <Tab.Screen name="CreateAccount">
                    {(props) => <CreateAccountScreen {...props} setIsLoggedIn={setIsLoggedIn} />}
                </Tab.Screen>
            </Tab.Navigator>
        );
    }

    // Code for checking which set of navigations to provide
    return (
        <View style={styles.container}>
            {isLoggedIn ? (
                <NormalScreen />
            ) : (
                <LoginScreenFunction />
            )}
        </View>
    );
}

// Style code
const styles = StyleSheet.create({
    // Styling to take the whole screen up
    container: {
        ...StyleSheet.absoluteFillObject,
    },
});