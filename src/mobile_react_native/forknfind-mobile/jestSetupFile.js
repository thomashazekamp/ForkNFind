// reference - Stack Overflow: https://stackoverflow.com/questions/55418910/jest-test-fails-after-installing-react-native-async-storage
jest.mock('@react-native-async-storage/async-storage', () => ({
  getItem: jest.fn(() => Promise.resolve(null)),
  setItem: jest.fn(() => Promise.resolve(null))
}));