import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import { create } from 'react-test-renderer';
import CreateAccountScreen from '../CreateAccountScreen';

describe('CreateAccountScreen', () => {

    it('Should have 1 children', () => {
        // check that the screen has 3 children
        const tree = create(<CreateAccountScreen />).toJSON();
        expect(tree.children.length).toBe(1);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<CreateAccountScreen />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Create Account', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Create Account')).toBeTruthy();
    });

    it('Should have Fill in your information to register an account', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Fill in your information to register an account')).toBeTruthy();
    });

    it('Should have Username', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Username')).toBeTruthy();
    });

    it('Should have First Name', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('First Name')).toBeTruthy();
    });

    it('Should have Last Name', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Last Name')).toBeTruthy();
    });

    it('Should have Email', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Email')).toBeTruthy();
    });

    it('Should have Password', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Password')).toBeTruthy();
    });

    it('Should have Retype Password', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Retype Password')).toBeTruthy();
    });

    it('Should have Sign Up', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Sign Up')).toBeTruthy();
    });

    it('Should have Sign in', () => {
        // render the review screen with a given data
        const { getByText } = render(<CreateAccountScreen />);
        // check that the screen has rendered
        expect(getByText('Sign In')).toBeTruthy();
    });
});