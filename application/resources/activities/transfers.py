from application import db
from application.models.activities.transfers import Transfer

def create_transfer(transfer_data):
    new_transfer = Transfer(
        item_id=transfer_data["item_id"],
        origin_id=transfer_data["origin_id"],
        destination_id=transfer_data["destination_id"],
        transfered_by=transfer_data["transfered_by"],
        reason=transfer_data.get("reason"),
        note=transfer_data.get("note"),
    )
    db.session.add(new_transfer)
    db.session.commit()
    return new_transfer

def get_all_transfers():
    return Transfer.query.all()

def get_transfer_by_id(transfer_id):
    return Transfer.query.get(transfer_id)

def update_transfer(transfer_id, transfer_data):
    transfer = Transfer.query.get(transfer_id)
    if transfer:
        transfer.item_id = transfer_data["item_id"]
        transfer.origin_id = transfer_data["origin_id"]
        transfer.destination_id = transfer_data["destination_id"]
        transfer.transfered_by = transfer_data["transfered_by"]
        transfer.reason = transfer_data.get("reason", transfer.reason)
        transfer.note = transfer_data.get("note", transfer.note)
        db.session.commit()
        return transfer
    return None

def delete_transfer(transfer_id):
    transfer = Transfer.query.get(transfer_id)
    if transfer:
        db.session.delete(transfer)
        db.session.commit()
        return True
    return False