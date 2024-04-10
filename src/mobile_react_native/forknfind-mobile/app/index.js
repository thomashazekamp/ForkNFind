import * as React from 'react';
import MainContainer from './navigation/MainContainer';
import { NavigationContainer } from '@react-navigation/native';
import { LogBox } from 'react-native';

LogBox.ignoreLogs(['Require cycle:']);

function App() {

    return (
        <NavigationContainer independent={true}>
            <MainContainer />
        </NavigationContainer>
    );
}

export default App;