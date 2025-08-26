export const idlFactory = ({ IDL }) => {
  const CanisterStatus = IDL.Record({
    'status' : IDL.Text,
    'memory_size' : IDL.Nat,
    'cycles' : IDL.Nat,
  });
  return IDL.Service({
    'get_status' : IDL.Func([IDL.Text], [IDL.Opt(CanisterStatus)], []),
  });
};
export const init = ({ IDL }) => { return []; };
