import os
import sys


import pygame

pygame.init() #initialises pygame, so the pygame.Font works

from src.constants import *

from src.util import *


def get_asset_path(relative_path):
    """ Get the absolute path to an asset, working for both dev and PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Example usage in your AssetManager.py around line 26:
# Instead of: pygame.image.load("assets/Overworld_Tileset.png")
# Use this:
tileset_path = get_asset_path(os.path.join("assets", "Overworld_Tileset.png"))
water_tile_path = get_asset_path(os.path.join("assets", "water_tile_anim_strip_8.png"))
edge_water_tile_path = get_asset_path(os.path.join("assets", "edge_water_tile_anim_strip_8.png"))

cursor_path = get_asset_path(os.path.join("assets", "gui", "cursors", "cursor.png"))
cursor_shadow_path = get_asset_path(os.path.join("assets", "gui", "cursors", "cursor_shadow.png"))
brush_path = get_asset_path(os.path.join("assets", "gui", "cursors", "brush.png"))
brush_shadow_path = get_asset_path(os.path.join("assets", "gui", "cursors", "brush_shadow.png"))
hammer_wrench_path = get_asset_path(os.path.join("assets", "gui", "cursors", "hammer_wrench.png"))
hammer_wrench_shadow_path = get_asset_path(os.path.join("assets", "gui", "cursors", "hammer_wrench_shadow.png"))

tile_focus_path = get_asset_path(os.path.join("assets", "gui", "focus", "tile_focus.png"))
_32x32_building_focus_path = get_asset_path(os.path.join("assets", "gui", "focus", "32x32_building_focus.png"))
_32x32_building_red_focus_path = get_asset_path(os.path.join("assets", "gui", "focus", "32x32_building_red_focus.png"))

select_editor_button_path = get_asset_path(os.path.join("assets", "gui", "buttons", "select_editor_button.png"))
select_editor_button_selected_path = get_asset_path(os.path.join("assets", "gui", "buttons", "select_editor_button_selected.png"))
terrain_editor_button_path = get_asset_path(os.path.join("assets", "gui", "buttons", "terrain_editor_button.png"))
terrain_editor_button_selected_path = get_asset_path(os.path.join("assets", "gui", "buttons", "terrain_editor_button_selected.png"))
accommodation_editor_button_path = get_asset_path(os.path.join("assets", "gui", "buttons", "accommodation_editor_button.png"))
accommodation_editor_button_selected_path = get_asset_path(os.path.join("assets", "gui", "buttons", "accommodation_editor_button_selected.png"))

grass_tile_brush_button_path = get_asset_path(os.path.join("assets", "gui", "buttons", "grass_tile_brush_button.png"))
grass_tile_brush_button_selected_path = get_asset_path(os.path.join("assets", "gui", "buttons", "grass_tile_brush_button_selected.png"))
dirt_tile_brush_button_path = get_asset_path(os.path.join("assets", "gui", "buttons", "dirt_tile_brush_button.png"))
dirt_tile_brush_button_selected_path = get_asset_path(os.path.join("assets", "gui", "buttons", "dirt_tile_brush_button_selected.png"))

accommodation_building_single_cardboard_box_path = get_asset_path(os.path.join("assets", "buildings", "single_cardboard_box.png"))

normal_font = get_asset_path(os.path.join("fonts", "pixelFont.ttf"))


gTextures = {
    #tileset
    "tileset":pygame.image.load(tileset_path),
    "water_tile":pygame.image.load(water_tile_path),
    "edge_water_tile":pygame.image.load(edge_water_tile_path),

    #special cursors
    "cursor":pygame.image.load(cursor_path),
    "cursor_shadow":pygame.image.load(cursor_shadow_path),
    "brush":pygame.image.load(brush_path),
    "brush_shadow":pygame.image.load(brush_shadow_path),
    "hammer_wrench":pygame.image.load(hammer_wrench_path),
    "hammer_wrench_shadow":pygame.image.load(hammer_wrench_shadow_path),

    #focus
    "tile_focus":pygame.image.load(tile_focus_path),
    "32x32_building_focus":pygame.image.load(_32x32_building_focus_path),
    "32x32_building_red_focus":pygame.image.load(_32x32_building_red_focus_path),


    #editor buttons

    "select_editor_button":pygame.image.load(select_editor_button_path),
    "select_editor_button_selected":pygame.image.load(select_editor_button_selected_path),
    "terrain_editor_button":pygame.image.load(terrain_editor_button_path),
    "terrain_editor_button_selected":pygame.image.load(terrain_editor_button_selected_path),
    "accommodation_editor_button":pygame.image.load(accommodation_editor_button_path),
    "accommodation_editor_button_selected":pygame.image.load(accommodation_editor_button_selected_path),


    
    #terrain editor buttons

    "grass_tile_brush_button":pygame.image.load(grass_tile_brush_button_path),
    "grass_tile_brush_button_selected":pygame.image.load(grass_tile_brush_button_selected_path),
    "dirt_tile_brush_button":pygame.image.load(dirt_tile_brush_button_path),
    "dirt_tile_brush_button_selected":pygame.image.load(dirt_tile_brush_button_selected_path),

    #accommodation buildings 


    "single_cardboard_box":pygame.image.load(accommodation_building_single_cardboard_box_path),



}
#combines the normal tileset, the water tileset and the water edge tileset into one tileset

gFrames = {
    "tileset":generateTileSets(gTextures["tileset"], TILE_WIDTH, TILE_HEIGHT) + generateTileSets(gTextures["water_tile"], TILE_WIDTH, TILE_HEIGHT) + generateTileSets(gTextures["edge_water_tile"], TILE_WIDTH, TILE_HEIGHT)
}



gFonts = {
    "normal_font":pygame.font.Font(normal_font, 11)
}