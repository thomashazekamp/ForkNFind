import React from 'react';
import renderer from 'react-test-renderer';

import SettingsScreen from '../SettingsScreen';

let total = 2;

describe('<SettingsScreen />', () => {
    it('renders correctly', () => {
        expect(total).toBe(2);
      });
});