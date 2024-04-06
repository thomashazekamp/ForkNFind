import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import { create } from 'react-test-renderer';
import SettingsScreen from '../SettingsScreen';

describe('SettingsScreen', () => {

    global.Platform = 'ios' // used to mock the platform
    global.access_global = 'token_test' // used to mock the access token

    it('Should have 5 children', () => {
        // check that the screen has 3 children
        const tree = create(<SettingsScreen />).toJSON();
        expect(tree.children.length).toBe(5);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<SettingsScreen />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Account Details', () => {
        // render the review screen with a given data
        const { getByText } = render(<SettingsScreen />);
        // check that the screen has rendered
        expect(getByText('Account Details')).toBeTruthy();
    });

    it('Should have Change Password', () => {
        // render the review screen with a given data
        const { getByText } = render(<SettingsScreen />);
        // check that the screen has rendered
        expect(getByText('Change Password')).toBeTruthy();
    });

    it('Should have Logout', () => {
        // render the review screen with a given data
        const { getByText } = render(<SettingsScreen />);
        // check that the screen has rendered
        expect(getByText('Logout')).toBeTruthy();
    });
});