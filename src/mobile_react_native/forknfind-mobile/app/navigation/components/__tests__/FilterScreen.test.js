import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import FilterScreen from '../FilterScreen';
import { create } from 'react-test-renderer';

describe('FilterScreen', () => {
    // mock the review data, needed for the screen
    const mockData = {
    current: {
        name: 'Test Name',
      },
    };

    global.Platform = 'ios' // used to mock the platform
    global.access_global = 'token_test' // used to mock the access token

    it('Should have 4 children', () => {
        // check that the screen has 3 children
        const tree = create(<FilterScreen searchQueryRef={mockData} />).toJSON();
        expect(tree.children.length).toBe(4);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<FilterScreen searchQueryRef={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have name', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Name')).toBeTruthy();
    });

    it('Should have address', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Address')).toBeTruthy();
    });

    it('Should have 4 above', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('4.0 and above')).toBeTruthy();
    });

    it('Should have 3 above', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('3.0 and above')).toBeTruthy();
    });

    it('Should have 2 above', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('2.0 and above')).toBeTruthy();
    });

    it('Should have 1 above', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('1.0 and above')).toBeTruthy();
    });

    it('Should have open', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Open')).toBeTruthy();
    });

    it('Should have Closed', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Closed')).toBeTruthy();
    });

    it('Should have attributes', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Attributes')).toBeTruthy();
    });

    it('Should have reset', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Reset')).toBeTruthy();
    });

    it('Should have apply', () => {
        // render the review screen with a given data
        const { getByText } = render(<FilterScreen searchQueryRef={mockData} />);
        // check that the screen has rendered
        expect(getByText('Apply')).toBeTruthy();
    });
});