import * as React from 'react';
import MainContainer from './navigation/MainContainer';
import { NavigationContainer } from '@react-navigation/native';

function App() {

    return (
        <NavigationContainer independent={true}>
            <MainContainer />
        </NavigationContainer>
    );
}

export default App;