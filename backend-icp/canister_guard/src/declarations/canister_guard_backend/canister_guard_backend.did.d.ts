import type { Principal } from '@dfinity/principal';
import type { ActorMethod } from '@dfinity/agent';
import type { IDL } from '@dfinity/candid';

export interface CanisterStatus {
  'status' : string,
  'memory_size' : bigint,
  'cycles' : bigint,
}
export interface _SERVICE {
  'get_status' : ActorMethod<[string], [] | [CanisterStatus]>,
}
export declare const idlFactory: IDL.InterfaceFactory;
export declare const init: (args: { IDL: typeof IDL }) => IDL.Type[];
