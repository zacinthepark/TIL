// Providing a type to querySelector:
const inputEl = document.querySelector<HTMLInputElement>("#username")!;
console.dir(inputEl);
inputEl.value = "Hacked!";

const btn = document.querySelector<HTMLButtonElement>(".btn")!;

// Without Generics...Lots of Repetition!
function numberIdentity(item: number): number {
  return item;
}
function stringIdentity(item: string): string {
  return item;
}
function booleanIdentity(item: boolean): boolean {
  return item;
}

// function identity(item: any): any{
//   return item;
// }

// With A Generic...Super Reusable!
function identity<T>(item: T): T {
  return item;
}

identity<number>(7);
identity<string>("hello");

function getRandomElement<T>(list: T[]): T {
  const randIdx = Math.floor(Math.random() * list.length);
  return list[randIdx];
}

console.log(getRandomElement<string>(["a", "b", "c"]));
getRandomElement<number>([5, 6, 21, 354, 567, 234, 654]);

// Generic Type Inference
getRandomElement([1, 2, 3, 4]);

// Generics With Constraints:
function merge<T extends object, U extends object>(object1: T, object2: U) {
  return {
    ...object1,
    ...object2,
  };
}

// Type Inference
const comboObj = merge({ name: "colt" }, { pets: ["blue", "elton"] });
console.log(merge({ name: "Colt" }, { num: 9 }));
// Without Type Inference
merge<{ name: string }, { pets: string[] }>(
  { name: "colt" },
  { pets: ["blue", "elton"] }
);

interface Lengthy {
  length: number;
}

// Generics With Custom Constraints:
function printDoubleLength<T extends Lengthy>(thing: T): number {
  return thing.length * 2;
}

// function printDoubleLength(thing: Lengthy): number {
//   return thing.length * 2;
// }

printDoubleLength("asdasd");
printDoubleLength(234); //Not allowed!

// Generics with Default Type
function makeEmptyArray<T = number>(): T[] {
  return [];
}

const nums = makeEmptyArray();
const bools = makeEmptyArray<boolean>();

// A Generic Class Example
interface Song {
  title: string;
  artist: string;
}
interface Video {
  title: string;
  creator: string;
  resolution: string;
}

class Playlist<T> {
  public queue: T[] = [];
  add(el: T) {
    this.queue.push(el);
  }
}

const songs = new Playlist<Song>();
const videos = new Playlist<Video>();
