import { types } from 'node:util';

export function repeatItems(values, times) {
  // Validate that values is a normal, dense array.
  if (
    types.isProxy(values) ||
    !Array.isArray(values) ||
    Object.getPrototypeOf(values) !== Array.prototype
  ) {
    throw new TypeError('values must be a normal array');
  }

  const length = values.length;

  // Validate every element before checking the repetition range.
  for (let i = 0; i < length; i++) {
    if (!Object.hasOwn(values, i) || typeof values[i] !== 'string') {
      throw new TypeError('values must contain only strings');
    }
  }

  // Validate the primitive number type.
  if (typeof times !== 'number') {
    throw new TypeError('times must be a primitive number');
  }

  // Validate the allowed range.
  if (!Number.isSafeInteger(times) || times < 0 || times > 10) {
    throw new RangeError('times must be a safe integer between 0 and 10');
  }

  // Repeat each string consecutively into a fresh array.
  const result = [];

  for (let i = 0; i < length; i++) {
    const value = values[i];

    for (let j = 0; j < times; j++) {
      result[result.length] = value;
    }
  }

  return result;
}
