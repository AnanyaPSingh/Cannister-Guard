import Principal "mo:base/Principal";
import Text "mo:base/Text";

persistent actor {
    public type CanisterStatusResponse = {
        status: { #running; #stopping; #stopped };
        memory_size: Nat;
        cycles: Nat;
    };

    transient let ic : actor {
        canister_status : ({ canister_id : Principal }) -> async CanisterStatusResponse;
    } = actor ("aaaaa-aa");

    public type CanisterStatus = {
        cycles: Nat;
        memory_size: Nat;
        status: Text;
    };

    public func get_status(canisterIdText: Text) : async ?CanisterStatus {
        let p = Principal.fromText(canisterIdText);

        let canister_status = await ic.canister_status({ canister_id = p });

        let status_text = switch (canister_status.status) {
            case (#running) { "running" };
            case (#stopping) { "stopping" };
            case (#stopped) { "stopped" };
        };

        return ?{
            cycles = canister_status.cycles;
            memory_size = canister_status.memory_size;
            status = status_text;
        };
    };
};
