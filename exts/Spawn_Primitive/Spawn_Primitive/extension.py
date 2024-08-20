import omni.ext
import omni.ui as ui
import omni.kit.commands

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[Spawn_Primitive] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class Spawn_primitiveExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[Spawn_Primitive] Spawn_Primitive startup")

        self._count = 0

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                        prim_type='Cube',
                        above_ground=True)
                   

                def move_cube():  
                   

                    omni.kit.commands.execute('TransformMultiPrimsSRTCpp',
                        count=1,
                        paths=['/World/Cube'],
                        new_translations=[172.15472685219325, 50.0, 0.0],
                        new_scales=[1.0, 1.0, 1.0]
                        )



                    label.text = "Clicked! "

               
                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=on_click)
                    ui.Button("Move Cube", clicked_fn=move_cube)

    def on_shutdown(self):
        print("[Spawn_Primitive] Spawn_Primitive shutdown")


