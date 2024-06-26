# utils/model_operations.py

import websockets
from utils.websocket_sender import VTubeStudioAPIWebsocketSender
from typing import List, Dict, Any

class VTSModelOperations:
    @staticmethod
    async def get_available_models(websocket: websockets.WebSocketClientProtocol) -> List[Dict[str, Any]]:
        models_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "getModels",
            "messageType": "AvailableModelsRequest"
        }
        models_response = await VTubeStudioAPIWebsocketSender.send_request(
            websocket, models_request)
        return models_response["data"]["availableModels"]

    @staticmethod
    async def load_model(websocket: websockets.WebSocketClientProtocol, model_id: str) -> Dict[str, Any]:
        load_model_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "loadModel",
            "messageType": "ModelLoadRequest",
            "data": {
                "modelID": model_id
            }
        }
        load_model_response = await VTubeStudioAPIWebsocketSender.send_request(
            websocket, load_model_request)
        return load_model_response

    @staticmethod
    async def move_model(websocket: websockets.WebSocketClientProtocol, 
                         position_x: float = 0, 
                         position_y: float = 0, 
                         rotation: float = 0, 
                         size: float = 0, 
                         time_in_seconds: float = 0.2, 
                         values_are_relative: bool = False) -> Dict[str, Any]:
        move_model_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "moveModel",
            "messageType": "MoveModelRequest",
            "data": {
                "timeInSeconds": time_in_seconds,
                "valuesAreRelativeToModel": values_are_relative,
                "positionX": position_x,
                "positionY": position_y,
                "rotation": rotation,
                "size": size
            }
        }
        move_model_response = await VTubeStudioAPIWebsocketSender.send_request(
            websocket, move_model_request)
        return move_model_response

    @staticmethod
    async def get_hotkeys(websocket: websockets.WebSocketClientProtocol, model_id: str = None) -> List[Dict[str, str]]:
        hotkeys_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "getHotkeys",
            "messageType": "HotkeysInCurrentModelRequest",
            "data": {}
        }
        if model_id:
            hotkeys_request["data"]["modelID"] = model_id
        
        hotkeys_response = await VTubeStudioAPIWebsocketSender.send_request(
            websocket, hotkeys_request)
        return hotkeys_response["data"]["availableHotkeys"]

    @staticmethod
    async def trigger_hotkey(websocket: websockets.WebSocketClientProtocol, hotkey_id: str) -> Dict[str, Any]:
        hotkey_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "triggerHotkey",
            "messageType": "HotkeyTriggerRequest",
            "data": {
                "hotkeyID": hotkey_id
            }
        }
        hotkey_response = await VTubeStudioAPIWebsocketSender.send_request(
            websocket, hotkey_request)
        return hotkey_response
